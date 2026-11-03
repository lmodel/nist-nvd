package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A product and which of its versions have the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdAffectedProduct  {

  private String defaultStatus;
  private String vendor;
  private String product;
  private URI collectionURL;
  private String packageName;
  private List<String> cpes;
  private List<String> modules;
  private List<String> programFiles;
  private List<NvdProgramRoutine> programRoutines;
  private List<String> platforms;
  private String repo;
  private List<NvdAffectedVersion> versions;
  private URI packageURL;


}
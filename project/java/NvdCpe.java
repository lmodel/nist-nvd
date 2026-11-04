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
  A CPE name as NVD holds it, with its UUID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCpe  {

  private String cpeName;
  private String cpeNameId;
  private ZonedDateTime created;
  private ZonedDateTime lastModified;
  private boolean deprecated;
  private List<NvdCpeTitle> titles;
  private List<NvdCpeReference> refs;
  private List<NvdCpeNameLink> deprecatedBy;
  private List<NvdCpeNameLink> deprecates;


}
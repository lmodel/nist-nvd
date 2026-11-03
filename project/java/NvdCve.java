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
  A vulnerability as NVD holds it, under its CVE identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCve  {

  private String id;
  private String sourceIdentifier;
  private ZonedDateTime lastModified;
  private List<NvdReference> references;
  private String vulnStatus;
  private ZonedDateTime published;
  private String evaluatorComment;
  private String evaluatorSolution;
  private String evaluatorImpact;
  private LocalDate cisaExploitAdd;
  private LocalDate cisaActionDue;
  private String cisaRequiredAction;
  private String cisaVulnerabilityName;
  private List<NvdCveTag> cveTags;
  private List<NvdLangString> descriptions;
  private NvdMetrics metrics;
  private List<NvdAffected> affected;
  private List<NvdWeakness> weaknesses;
  private List<NvdConfiguration> configurations;
  private List<NvdVendorComment> vendorComments;


}